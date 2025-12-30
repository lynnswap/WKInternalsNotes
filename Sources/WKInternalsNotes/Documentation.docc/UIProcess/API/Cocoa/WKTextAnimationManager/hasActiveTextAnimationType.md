# ``WKInternalsNotes/WKTextAnimationManager/hasActiveTextAnimationType()``

アクティブなテキストアニメーションがあるかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)hasActiveTextAnimationType;
```

## Discussion
`_chunkToEffect` の件数が 0 以外かどうかを返す。

## References
- [`WKTextAnimationManagerMac.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextAnimationManagerMac.h#L48)
- [`WKTextAnimationManagerMac.mm#L202`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextAnimationManagerMac.mm#L202)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
