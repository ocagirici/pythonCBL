from Goulib.geom import Point3, Sphere

s = Sphere(Point3(1.0, 1.0, 1.0), 0.5)
t = Sphere(Point3(2.0, 2.0, 2.0), 0.5)

#s.intersect(t)
c1 = Point3(0, 0, 0)
c2 = Point3(0, 1, 1)
c3 = Point3(3, 0, 3)
r1 = 1
r2 = 2
r3 = 0.4

s1 = Sphere(c1, r1)
s2 = Sphere(c2, r2)
s3 = Sphere(c3, r3)

s1.intersect(s2)


