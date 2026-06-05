package com.vesper.genesis

class BraidBridge {
    init {
        System.loadLibrary("braidc")
    }

    external fun igniteSilicon(): String
}
