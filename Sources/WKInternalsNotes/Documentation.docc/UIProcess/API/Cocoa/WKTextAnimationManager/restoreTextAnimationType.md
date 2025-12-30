# ``WKInternalsNotes/WKTextAnimationManager/restoreTextAnimationType()``

`Initial` タイプのアニメーションを再追加する。

## Objective-C Declaration
```objective-c
- (void)restoreTextAnimationType;
```

## Discussion
`_chunkToEffect` のうち `Initial` タイプのものを `addTextAnimationForAnimationID:withData:` で再登録する。

## References
- [`WKTextAnimationManagerMac.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextAnimationManagerMac.h#L51)
- [`WKTextAnimationManagerMac.mm#L218`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextAnimationManagerMac.mm#L218)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
