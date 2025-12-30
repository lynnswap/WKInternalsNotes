# ``WKInternalsNotes/_WKWarningView/initWithFrame(_:browsingWarning:completionHandler:)``

警告表示用のビューを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithFrame:(RectType)frame browsingWarning:(const WebKit::BrowsingWarning&)warning completionHandler:(CompletionHandler<void(Variant<WebKit::ContinueUnsafeLoad, URL>&&)>&&)completionHandler;
```

## Discussion
`[super initWithFrame:]` に失敗すると `completionHandler(ContinueUnsafeLoad::Yes)` を呼んで `nil` を返す。成功時は `_completionHandler` をラップして `_warning` を保持し、背景色や内容ビューを設定する。

## References
- [`_WKWarningView.h#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/_WKWarningView.h#L80)
- [`_WKWarningView.mm#L314`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/_WKWarningView.mm#L314)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
