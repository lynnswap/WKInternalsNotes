# ``WKInternalsNotes/WKContentView/_beginPointerLockMouseTracking()``

ポインタロック開始時にマウストラッキングを開始する。

## Objective-C Declaration
```objective-c
- (void)_beginPointerLockMouseTracking;
```

## Discussion
`ENABLE(POINTER_LOCK)` かつ `HAVE(UIKIT_WITH_MOUSE_SUPPORT)` のとき、`_mouseInteraction` に対して `beginPointerLockMouseTracking` を呼ぶ。

## References
- [WKContentViewInteraction.h#L1091](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1091)
- [WKContentViewInteraction.mm#L14389](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14389)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
