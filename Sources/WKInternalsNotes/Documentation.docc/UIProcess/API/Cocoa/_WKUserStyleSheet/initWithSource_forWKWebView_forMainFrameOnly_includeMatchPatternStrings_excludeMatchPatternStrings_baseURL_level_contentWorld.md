# ``WKInternalsNotes/_WKUserStyleSheet/initWithSource(_:forWKWebView:forMainFrameOnly:includeMatchPatternStrings:excludeMatchPatternStrings:baseURL:level:contentWorld:)``

追加条件付きでユーザースタイルシートを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithSource:(NSString *)source forWKWebView:(nullable WKWebView *)webView forMainFrameOnly:(BOOL)forMainFrameOnly includeMatchPatternStrings:(nullable NSArray<NSString *> *)includeMatchPatternStrings excludeMatchPatternStrings:(nullable NSArray<NSString *> *)excludeMatchPatternStrings baseURL:(nullable NSURL *)baseURL level:(_WKUserStyleLevel)level contentWorld:(nullable WKContentWorld *)contentWorld;
```

## Discussion
WebKit 初期化後に `API::UserStyleSheet` を構築する。include/exclude パターン、`baseURL`、スタイルレベル、対象ページ ID（`webView` がある場合）、および `contentWorld` を反映する。

## References
- [`_WKUserStyleSheet.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserStyleSheet.h#L51)
- [`_WKUserStyleSheet.mm#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserStyleSheet.mm#L54)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
