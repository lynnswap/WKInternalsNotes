# ``WKInternalsNotes/_WKDataTaskDelegate/dataTask(_:didCompleteWithError:)``

タスク完了を通知する。

## Objective-C Declaration
```objective-c
- (void)dataTask:(_WKDataTask *)dataTask didCompleteWithError:(nullable NSError *)error;
```

## Discussion
完了時に `NSError` を渡して通知し、delegate 参照を `nil` にして解放する。

## References
- [`_WKDataTaskDelegate.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTaskDelegate.h#L53)
- [`_WKDataTask.mm#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L111)
- [`_WKDataTask.mm#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L117)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
