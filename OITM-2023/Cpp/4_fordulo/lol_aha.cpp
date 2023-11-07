#include <iostream>

// vvvvvvvvvvvvv AFTER THIS vvvvvvvvvvvvv
/*  1 */ class Base
/*  2 */ {
/*  3 */ public:
/*  4 */     Base() { std::cout << 'L'; }
/*  5 */     Base(const Base &) { std::cout << 'H'; }
/*  6 */     ~Base() { std::cout << 'A'; }
/*  7 */ };
/*  8 */
/*  9 */ class Derived : public Base
/* 10 */ {
/* 11 */ public:
/* 12 */     Derived() { std::cout << 'O'; }
/* 13 */     Derived(const Derived &) { std::cout << ' '; }
/* 14 */     ~Derived() { std::cout << 'H'; }
/* 15 */ };
// vvvvvvvvvvvvv BEFORE THIS vvvvvvvvvvvv

int main()
{
    Derived a;
    Base *d = new Derived(a);
    delete d;
    return 0;
}
