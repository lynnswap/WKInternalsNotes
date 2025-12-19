# ``WKInternalsNotes/WKWebView/_requestTextExtractionInternal(_:completion:)``

text extraction の内部リクエストを発行する。

## Objective-C Declaration
```objective-c
- (void)_requestTextExtractionInternal:(_WKTextExtractionConfiguration *)configuration completion:(CompletionHandler<void(std::optional<WebCore::TextExtraction::Item>&&)>&&)completion;
```

## Discussion
- `textExtractionEnabled` が無効、または WebView が無効な場合は空の結果を返す。
- `targetRect` を root view 座標に変換し、`TextExtraction::Request` を構築して `_page->requestTextExtraction` に委譲する。
- `USE(APPLE_INTERNAL_SDK)` もしくは watchOS/Apple TV 以外でのみ有効。

## References
- [`WKWebView.mm#L331`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L331)
- [`WKWebView.mm#L331`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L331)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
