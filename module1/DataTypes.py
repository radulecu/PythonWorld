if __name__ == '__main__':
    s1 = "Just a String"
    f = 123.456
    f2=1.0
    i = 1
    b = True
    print(s1, type(s1))
    print(f, type(f))
    print(f2, type(f2))
    print(i, type(i))
    print(b, type(b))
    f2i = int(f)
    i2f = float(i)
    print("f->i", f2i, type(f2i))
    print("i->f", i2f, type(i2f))
    im12b=bool(-1)
    i02b=bool(0)
    i12b=bool(1)
    i22b=bool(2)
    print("-1->b", im12b, type(im12b))
    print("0->b", i02b, type(i02b))
    print("1->b", i12b, type(i12b))
    print("2->b", i22b, type(i22b))
    i2s = str(i)
    f2s = str(f)
    b2s = str(b)
    print("i->s", i2s, type(i2s))
    print("f->s", f2s, type(f2s))
    print("b->s", b2s, type(b2s))
    s2 = 12.34
    s22i = int(s2)
    s22f = float(s2)
    print("s->i", s22i, type(s22i))
    print("s->f", s22f, type(s22f))
    s3 = "False"
    s32b = bool(s3)
    print("s->b",s32b, type(s32b))
    s2i = float(s1)
