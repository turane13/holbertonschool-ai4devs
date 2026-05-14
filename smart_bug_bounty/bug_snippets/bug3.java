public class StringComparison {
    public static boolean checkPassword(String input, String correctPassword) {
        if (input == null || correctPassword == null) {
            return false;
        }
        
        if (input == correctPassword) {
            return true;
        }
        
        return false;
    }
}
