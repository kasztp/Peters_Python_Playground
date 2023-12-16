import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.lang.reflect.Field;

public class ClassLoaderFeladat {

  public static void main(String[] args) throws Exception {
    SajatTitkositottClassLoader loader = new SajatTitkositottClassLoader("OITM2023JAVA2023");
    Class<?> loadedClass = loader.findClass("Echelon");
    Field noise5Field = loadedClass.getDeclaredField("noise5");
    System.out.println("The type of the 'noise5' field is: " + noise5Field.getType());
}
}

class SajatTitkositottClassLoader extends ClassLoader {
  private static final String ALGORITHM = "AES";
  private final String key;

  public SajatTitkositottClassLoader(String key) {
    this.key = key;
  }

  @Override
  protected Class<?> findClass(String name) throws ClassNotFoundException {
    byte[] classData = getClassData(name);
    if (classData == null) {
      throw new ClassNotFoundException();
    }
    return defineClass(name, classData, 0, classData.length);
  }

  public byte[] getClassData(String className) {
    String path = className.replace('.', '/') + ".enc";
    try {
      byte[] encryptedData = getBytesFromFile(new File(path));
      return decrypt(encryptedData);
    } catch (Exception e) {
      e.printStackTrace();
      return null;
    }
  }

  private byte[] decrypt(byte[] encryptedData) throws Exception {
    SecretKey secretKey = new SecretKeySpec(key.getBytes(), ALGORITHM);
    Cipher cipher = Cipher.getInstance(ALGORITHM);
    cipher.init(Cipher.DECRYPT_MODE, secretKey);

    return cipher.doFinal(encryptedData);
  }

  private byte[] getBytesFromFile(File file) throws IOException {
    try (FileInputStream fis = new FileInputStream(file)) {
      byte[] bytes = new byte[(int) file.length()];
      fis.read(bytes);
      return bytes;
    }
  }
}
