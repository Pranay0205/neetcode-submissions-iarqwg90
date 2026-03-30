public class DynamicArray {
    
    int capacity;
    int size;
    int[] array;

    public DynamicArray(int capacity) {
        if (capacity > 0){
            this.capacity = capacity;
            this.array = new int[this.capacity];
            this.size = 0;
        }       
    }

    public int Get(int i) {
        return array[i];
    }

    public void Set(int i, int n) {
        array[i] = n;
    }


   

    public void PushBack(int n) {
        if(size == capacity){
            Resize();
        }
        array[size] = n;
        size++;
    }

    public int PopBack() {
        if(size > 0){
            size--;
        }
        
        return array[size];
    }

    private void Resize() {

        int newCapacity = capacity * 2;

        int[] tempArray = new int[capacity * 2];

        for(int i = 0; i < size; i++){
            tempArray[i] = array[i];
        }

        array = tempArray;
        capacity = newCapacity;

    }  

    public int GetSize() {
        return size;
    }

    public int GetCapacity() {
        return capacity;
    }
}
