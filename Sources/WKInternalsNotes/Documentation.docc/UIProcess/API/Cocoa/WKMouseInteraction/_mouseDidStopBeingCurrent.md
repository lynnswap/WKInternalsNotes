# ``WKInternalsNotes/WKMouseInteraction/_mouseDidStopBeingCurrent(_:)``

ポインタロック中のマウス切断を処理する。

## Objective-C Declaration
```objective-c
- (void)_mouseDidStopBeingCurrent:(NSNotification *)notification;
```

## Discussion
ロックが有効な場合にデリゲートへ通知し、ポインタロックを終了する。

## References
- [`WKMouseInteraction.mm#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L73)
- [`WKMouseInteraction.mm#L530`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L530)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
