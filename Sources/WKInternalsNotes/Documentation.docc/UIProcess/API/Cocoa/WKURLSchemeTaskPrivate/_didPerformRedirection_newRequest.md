# ``WKInternalsNotes/WKURLSchemeTaskPrivate/_didPerformRedirection(_:newRequest:)``

リダイレクト完了を URL scheme task に通知する。

## Objective-C Declaration
```objective-c
- (void)_didPerformRedirection:(NSURLResponse *)response newRequest:(NSURLRequest *)request;
```

## Discussion
内部の `WebURLSchemeTask::didPerformRedirection` を呼び出し、メインループ経由の実行結果に応じて例外を処理する。

## References
- [`WKURLSchemeTaskPrivate.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKURLSchemeTaskPrivate.h#L47)
- [`WKURLSchemeTask.mm#L158`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKURLSchemeTask.mm#L158)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
