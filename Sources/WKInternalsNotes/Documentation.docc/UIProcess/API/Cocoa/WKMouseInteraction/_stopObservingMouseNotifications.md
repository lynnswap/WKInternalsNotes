# ``WKInternalsNotes/WKMouseInteraction/_stopObservingMouseNotifications()``

マウス通知の監視を停止する。

## Objective-C Declaration
```objective-c
- (void)_stopObservingMouseNotifications;
```

## Discussion
監視中のみ `GCMouseDidStopBeingCurrentNotification` のオブザーバを解除し、フラグを `false` にする。

## References
- [`WKMouseInteraction.mm#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L72)
- [`WKMouseInteraction.mm#L522`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L522)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
