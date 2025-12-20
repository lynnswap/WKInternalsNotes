# ``WKInternalsNotes/WKBaseScrollView/axesToPreventMomentumScrolling``

モメンタムスクロールを抑止する軸を示す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UIAxis axesToPreventMomentumScrolling;
```

## Default Value
`initWithFrame:` で `UIAxisNeither` に初期化される。

## Discussion
`_updatePanGestureToPreventScrolling` で translation が調整された軸を OR で蓄積し、次回のパン開始時にリセットされる。

## References
- [`WKBaseScrollView.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.h#L56)
- [`WKBaseScrollView.mm#L136`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.mm#L136)
- [`WKBaseScrollView.mm#L213`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.mm#L213)
- [`WKBaseScrollView.mm#L287`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.mm#L287)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
