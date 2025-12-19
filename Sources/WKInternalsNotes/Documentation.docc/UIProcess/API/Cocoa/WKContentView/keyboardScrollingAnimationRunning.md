# ``WKInternalsNotes/WKContentView/keyboardScrollingAnimationRunning``

キーボードスクロールのアニメーション中かを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isKeyboardScrollingAnimationRunning) BOOL keyboardScrollingAnimationRunning;
```

## Default Value
`_isKeyboardScrollingAnimationRunning` を返す。

## Discussion
`WKKeyboardScrollViewAnimator` の開始/終了で更新されるフラグの getter。

## References
- [`WKContentViewInteraction.h#L739`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L739)
- [`WKContentViewInteraction.mm#L7888`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7888)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
