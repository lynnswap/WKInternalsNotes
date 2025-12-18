# ``WKInternalsNotes/WKWebViewConfiguration/_shouldDeferAsynchronousScriptsUntilAfterDocumentLoad``

async script を document load 後に遅延

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setShouldDeferAsynchronousScriptsUntilAfterDocumentLoad:) BOOL _shouldDeferAsynchronousScriptsUntilAfterDocumentLoad WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_shouldDeferAsynchronousScriptsUntilAfterDocumentLoad = YES`: async script を document load 後に遅延。
- `_shouldDeferAsynchronousScriptsUntilAfterDocumentLoad = NO`: async script を document load 後に遅延（無効）。

## References
- [`WKWebViewConfigurationPrivate.h#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L97)
- [`WKWebViewConfiguration.mm#L1070`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1070)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
