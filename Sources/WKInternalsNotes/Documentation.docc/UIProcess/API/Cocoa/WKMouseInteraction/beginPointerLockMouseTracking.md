# ``WKInternalsNotes/WKMouseInteraction/beginPointerLockMouseTracking()``

ポインタロックのマウストラッキングを開始する。

## Objective-C Declaration
```objective-c
- (void)beginPointerLockMouseTracking;
```

## Discussion
マウスデバイスが存在し、`GCMouse` が取得できる場合に観測を開始し、ホバーを無効化してロック状態に入る。

## References
- [`WKMouseInteraction.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.h#L50)
- [`WKMouseInteraction.mm#L449`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L449)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
