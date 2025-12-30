# ``WKInternalsNotes/WKTextAnimationManager/removeTextAnimationForAnimationID(_:)``

指定 ID のエフェクトを削除する。

## Objective-C Declaration
```objective-c
- (void)removeTextAnimationForAnimationID:(NSUUID *)uuid;
```

## Discussion
`_chunkToEffect` から `effectID` を取得して `_effectView` から削除し、辞書から取り除く。

## References
- [`WKTextAnimationManagerMac.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextAnimationManagerMac.h#L44)
- [`WKTextAnimationManagerMac.mm#L188`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextAnimationManagerMac.mm#L188)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
