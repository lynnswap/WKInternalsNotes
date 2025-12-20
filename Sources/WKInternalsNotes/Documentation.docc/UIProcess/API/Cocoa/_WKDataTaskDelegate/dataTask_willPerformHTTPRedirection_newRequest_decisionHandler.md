# ``WKInternalsNotes/_WKDataTaskDelegate/dataTask(_:willPerformHTTPRedirection:newRequest:decisionHandler:)``

リダイレクト可否を delegate で決定する。

## Objective-C Declaration
```objective-c
- (void)dataTask:(_WKDataTask *)dataTask willPerformHTTPRedirection:(NSHTTPURLResponse *)response newRequest:(NSURLRequest *)request decisionHandler:(void (^)(_WKDataTaskRedirectPolicy))decisionHandler;
```

## Discussion
delegate が未実装の場合は `Allow` として扱う。実装されている場合は `_WKDataTaskRedirectPolicy` を `bool` に変換して処理する。

## References
- [`_WKDataTaskDelegate.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTaskDelegate.h#L50)
- [`_WKDataTask.mm#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L75)
- [`_WKDataTask.mm#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L81)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
