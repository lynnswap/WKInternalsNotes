# ``WKInternalsNotes/_WKWarningView/initWithFrame(_:browsingWarning:completionHandler:)``

宣言のみ確認（実装未調査）。

## Objective-C Declaration
```objective-c
- (instancetype)initWithFrame:(RectType)frame browsingWarning:(const WebKit::BrowsingWarning&)warning completionHandler:(CompletionHandler<void(Variant<WebKit::ContinueUnsafeLoad, URL>&&)>&&)completionHandler;
```

## Discussion
実装未調査。宣言と対応実装の確認が必要。

## References
- [`_WKWarningView.h#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/_WKWarningView.h#L80)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
