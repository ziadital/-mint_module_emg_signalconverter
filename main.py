@namespace
class EMGConversion:
    bufferSize = 10
    # Anzahl der Werte, über die der RMS-Wert berechnet wird
    buffer: List[number] = []
    """
    
    Filters, rectifies, and calculates the RMS of the EMG signal over a short time window
    @param signal The raw EMG signal
    @returns The RMS of the EMG signal over the short time window
    
    """
    # % block="Filter RAW Signal $signal"
    # % signal.min=0 signal.max=1023
    def convertFilterRectifyAndCalculateRMS(signal: number):
        # Filter and rectify the signal (in this example, the filter is just taking the absolute value)
        filteredSignal = abs(signal)
        # Add the filtered signal to the buffer
        buffer.append(filteredSignal)
        # If the buffer size exceeds the specified size, remove the oldest value
        if len(buffer) > bufferSize:
            buffer.shift()
        # Calculate the sum of squares of the buffer values
        def on_reduce(acc, val):
            pass
        sumOfSquares = buffer.reduce(on_reduce, 0)
        # Calculate RMS (Root Mean Square) value
        rms = Math.sqrt(sumOfSquares / len(buffer))
        return rms