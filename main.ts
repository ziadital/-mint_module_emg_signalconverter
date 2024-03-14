namespace EMGConversion {
    const bufferSize = 10; // Anzahl der Werte, über die der RMS-Wert berechnet wird
    let buffer: number[] = [];

    /**
     * Filters, rectifies, and calculates the RMS of the EMG signal over a short time window
     * @param signal The raw EMG signal
     * @returns The RMS of the EMG signal over the short time window
     */
    //% block="Filter RAW Signal $signal"
    //% signal.min=0 signal.max=1023
    export function convertFilterRectifyAndCalculateRMS(signal: number): number {
        // Filter and rectify the signal (in this example, the filter is just taking the absolute value)
        const filteredSignal = Math.abs(signal);

        // Add the filtered signal to the buffer
        buffer.push(filteredSignal);

        // If the buffer size exceeds the specified size, remove the oldest value
        if (buffer.length > bufferSize) {
            buffer.shift();
        }

        // Calculate the sum of squares of the buffer values
        const sumOfSquares = buffer.reduce((acc, val) => acc + val * val, 0);

        // Calculate RMS (Root Mean Square) value
        const rms = Math.sqrt(sumOfSquares / buffer.length);

        return rms;
    }
}
