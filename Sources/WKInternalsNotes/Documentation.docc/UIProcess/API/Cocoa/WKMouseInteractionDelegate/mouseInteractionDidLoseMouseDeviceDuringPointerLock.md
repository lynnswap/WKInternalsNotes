# ``WKInternalsNotes/WKMouseInteractionDelegate/mouseInteractionDidLoseMouseDeviceDuringPointerLock(_:)``

ポインタロック中にマウスデバイスを失ったことを通知する。

## Objective-C Declaration
```objective-c
- (void)mouseInteractionDidLoseMouseDeviceDuringPointerLock:(WKMouseInteraction *)interaction;
```

## Discussion
ポインタロック中にマウスが切断された通知を受けると呼ばれ、`endPointerLockMouseTracking` が実行される。

## References
- [`WKMouseInteraction.mm#L530`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L530)
- [`WKMouseInteraction.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.h#L38)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
