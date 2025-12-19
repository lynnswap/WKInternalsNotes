# ``WKInternalsNotes/_WKDataTaskDelegate/dataTask(_:willPerformHTTPRedirection:newRequest:decisionHandler:)``

宣言のみ確認（実装未調査）。

## Objective-C Declaration
```objective-c
- (void)dataTask:(_WKDataTask *)dataTask willPerformHTTPRedirection:(NSHTTPURLResponse *)response newRequest:(NSURLRequest *)request decisionHandler:(void (^)(_WKDataTaskRedirectPolicy))decisionHandler;
```

## Discussion
実装未調査。宣言と対応実装の確認が必要。

## References
- [`_WKDataTaskDelegate.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTaskDelegate.h#L47)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
