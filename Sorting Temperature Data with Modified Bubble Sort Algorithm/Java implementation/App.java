package y;


public class App 
{
    public static int[] bubbleSortTemperatures(int[] temperatureData) {
        int n = temperatureData.length;

        for (int i = 0; i < n; i++) {
            boolean swapped = false;
            for (int j = 1; j < n; j++) {
                if (temperatureData[j] < temperatureData[j - 1]) {
                    int temp = temperatureData[j];
                    temperatureData[j] = temperatureData[j - 1];
                    temperatureData[j - 1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) {
                System.out.println("Algorithm stopped at stage " + i);
                break;
            }
        }

        return temperatureData;
    }

    public static void main( String[] args )
    {
        int[] temperatureData = {-7, 12, 24, 15, 3, -1, 14, 6};
        int[] sortedTemperatureData = bubbleSortTemperatures(temperatureData);

        System.out.print("Sorted temperature data: ");
        for (int temperature : sortedTemperatureData) {
            System.out.print(temperature + " ");
    }
}
}
