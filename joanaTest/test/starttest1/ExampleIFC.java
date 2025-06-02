package test.starttest1;

public class ExampleIFC {

    public static void main(String[] args) {
        String secret = getSecret(); // high security level source
        System.out.println(secret);  // low security level sink, will cause a warning
    }

    public static String getSecret() {
        return "TopSecret";
    }

    public static void sendToNetwork(String data) {
        System.out.println(data);
    }
}
