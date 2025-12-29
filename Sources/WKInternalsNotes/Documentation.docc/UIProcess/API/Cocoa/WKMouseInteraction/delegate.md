# ``WKInternalsNotes/WKMouseInteraction/delegate``

マウスイベントを受け取るデリゲート。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, weak) id <WKMouseInteractionDelegate> delegate;
```

## Default Value
`initWithDelegate:` で渡した値（`weak`）。

## Discussion
初期化時に `_delegate` を設定し、以降のマウスイベント通知に使用する。

## References
- [`WKMouseInteraction.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.h#L44)
- [`WKMouseInteraction.mm#L150`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L150)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
