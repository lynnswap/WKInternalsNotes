# ``WKInternalsNotes/_WKUserStyleSheet/initWithSource(_:forMainFrameOnly:)``

CSS ソースを指定してユーザースタイルシートを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithSource:(NSString *)source forMainFrameOnly:(BOOL)forMainFrameOnly;
```

## Discussion
WebKit 初期化後に `API::UserStyleSheet` を構築する。`forMainFrameOnly` に応じて `InjectInTopFrameOnly` または `InjectInAllFrames` を設定し、`User` レベルかつ page content world を使用する。

## References
- [`_WKUserStyleSheet.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserStyleSheet.h#L49)
- [`_WKUserStyleSheet.mm#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserStyleSheet.mm#L42)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
