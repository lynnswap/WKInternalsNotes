# ``WKInternalsNotes/_WKTextExtractionInteraction/debugDescriptionInWebView(_:completionHandler:)``

指定した `WKWebView` でのデバッグ記述を取得する。

## Objective-C Declaration
```objective-c
- (void)debugDescriptionInWebView:(WKWebView *)webView completionHandler:(void (^)(NSString * _Nullable, NSError * _Nullable))completionHandler;
```

## Discussion
`WKWebView` の `_describeInteraction:completionHandler:` を呼び出して、説明文字列とエラーを返す。

## References
- [`_WKTextExtraction.mm#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.mm#L97)
- [`_WKTextExtraction.h#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.h#L80)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
