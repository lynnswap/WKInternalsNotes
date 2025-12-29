# ``WKInternalsNotes/WKMouseInteraction/_startObservingMouseNotifications()``

pointer lock 中のマウス通知監視を開始する。

## Objective-C Declaration
```objective-c
- (void)_startObservingMouseNotifications;
```

## Discussion
既に監視中なら何もしない。`GCMouseDidStopBeingCurrent` 通知を監視し、監視フラグを `true` にする。

## References
- [`WKMouseInteraction.mm#L513`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L513)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
