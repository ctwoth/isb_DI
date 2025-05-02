import java.util.Random;

public class randomSequence {
    public static void main(String[] args) {
        Random random = new Random();
        StringBuilder randSequence = new StringBuilder();

        System.out.println("Sequence: ");

        for (int i = 0; i < 128; ++i) {
            randSequence.append(random.nextInt(2));
        }

        System.out.println(randSequence.toString());
    }
}
