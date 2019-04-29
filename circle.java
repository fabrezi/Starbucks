//basics of OOP with use of constructors

public class circle {
    public static void main(String[] args){

        //object1 to create
        circle c1 = new circle();
        System.out.println("area: " + c1.radius + " is " + c1.getArea());

        //object2 create
        circle c2 = new circle();
        System.out.println("area2: " + c2.radius + c2.getArea());
    }

    double radius;

    //no-arg constructor
    circle(){
        radius =1;
    }

    //constructor
    circle(double newradius){
        radius = newradius;
    }

    //method
    double getArea(){
        return radius * radius * Math.PI;
    }

    //set the new radius
    void setRadius(double newradius){
        radius = newradius;
    }


}
