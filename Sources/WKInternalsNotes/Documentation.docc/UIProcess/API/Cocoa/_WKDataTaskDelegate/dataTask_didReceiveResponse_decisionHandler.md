# ``WKInternalsNotes/_WKDataTaskDelegate/dataTask(_:didReceiveResponse:decisionHandler:)``

レスポンス受信可否を delegate で決定する。

## Objective-C Declaration
```objective-c
- (void)dataTask:(_WKDataTask *)dataTask didReceiveResponse:(NSURLResponse *)response decisionHandler:(void (^)(_WKDataTaskResponsePolicy))decisionHandler;
```

## Discussion
delegate が未実装の場合は `Allow` として扱う。実装されている場合は `_WKDataTaskResponsePolicy` を `bool` に変換して処理する。

## References
- [`_WKDataTaskDelegate.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTaskDelegate.h#L51)
- [`_WKDataTask.mm#L89`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L89)
- [`_WKDataTask.mm#L95`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L95)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
