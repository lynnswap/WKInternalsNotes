# ``WKInternalsNotes/WKContentView/_endPointerLockMouseTracking()``

ポインタロック終了時にマウストラッキングを停止する。

## Objective-C Declaration
```objective-c
- (void)_endPointerLockMouseTracking;
```

## Discussion
`ENABLE(POINTER_LOCK)` かつ `HAVE(UIKIT_WITH_MOUSE_SUPPORT)` のとき、`_mouseInteraction` に対して `endPointerLockMouseTracking` を呼ぶ。

## References
- [WKContentViewInteraction.h#L1092](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1092)
- [WKContentViewInteraction.mm#L14396](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14396)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
