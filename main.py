namespace EMGConversion {
    const windowSize = 10; // Größe des Zeitfensters
    let signalBuffer: number[] = [];

    /**
     * Filters, rectifies, and calculates the RMS of the EMG signal over a window of the specified size
     * @param signal The raw EMG signal
     * @returns The RMS of the EMG signal over the specified window
     */
    //% block="Filter RAW Signal $signal"
    //% signal.min=0 signal.max=1023
    export function convertFilterRectifyAndCalculateRMS(signal: number): number {
        // Filter and rectify the signal (in this example, the filter is just taking the absolute value)
        const filteredSignal = Math.abs(signal);

        // Add the filtered signal to the buffer
        signalBuffer.push(filteredSignal);

        // If the buffer size exceeds the window size, remove oldest elements
        if (signalBuffer.length > windowSize) {
            signalBuffer.shift(); // Remove oldest element
        }

        // Calculate the sum of squares over the window
        const sumOfSquares = signalBuffer.reduce((acc, val) => acc + (val * val), 0);

        // Calculate RMS (Root Mean Square) value over the window
        const rms = Math.sqrt(sumOfSquares / signalBuffer.length);

        return rms;
    }
}
