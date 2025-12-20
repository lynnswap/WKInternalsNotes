# ``WKInternalsNotes/_WKDataTaskDelegate/dataTask(_:didReceiveData:)``

受信データを通知する。

## Objective-C Declaration
```objective-c
- (void)dataTask:(_WKDataTask *)dataTask didReceiveData:(NSData *)data;
```

## Discussion
`std::span` で受け取ったデータを `NSData` に変換して delegate に渡す。

## References
- [`_WKDataTaskDelegate.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTaskDelegate.h#L52)
- [`_WKDataTask.mm#L103`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L103)
- [`_WKDataTask.mm#L108`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L108)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
