# Deserialize the serialized java data object from enigma.obj
# and print the result
import jpype
import os

enigma_path = os.path.join(os.getcwd(), "Enigma.class")

# Start the JVM
jpype.startJVM(jpype.getDefaultJVMPath(), f"-Djava.class.path={enigma_path}")


# Get the classes from java.io package
FileInputStream = jpype.JClass("java.io.FileInputStream")
ObjectInputStream = jpype.JClass("java.io.ObjectInputStream")

# Get the Enigma class
Enigma = jpype.JClass("Enigma")

# Create a FileInputStream and ObjectInputStream
fis = FileInputStream(os.path.join(os.getcwd(), "enigma.obj"))
ois = ObjectInputStream(fis)

# Read the object
pobj = ois.readObject()

# Print the object
print(pobj)

# Close the streams
ois.close()
fis.close()

# Shutdown the JVM
jpype.shutdownJVM()

"D:\github_projects\Peters_Python_Playground\OITM-2023\java"