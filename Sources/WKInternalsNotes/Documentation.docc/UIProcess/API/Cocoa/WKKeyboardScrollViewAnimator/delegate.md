# ``WKInternalsNotes/WKKeyboardScrollViewAnimator/delegate``

スクロール判定を行う delegate を設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id <WKKeyboardScrollViewAnimatorDelegate> delegate;
```

## Discussion
`delegate` を保持し、`isScrollableForKeyboardScrollViewAnimator:` などの optional メソッドに応答するかどうかをキャッシュしておく。

## References
- [`WKKeyboardScrollingAnimator.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.h#L54)
- [`WKKeyboardScrollingAnimator.mm#L597`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L597)
- [`WKKeyboardScrollingAnimator.mm#L601`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L601)
- [`WKKeyboardScrollingAnimator.mm#L604`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L604)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
