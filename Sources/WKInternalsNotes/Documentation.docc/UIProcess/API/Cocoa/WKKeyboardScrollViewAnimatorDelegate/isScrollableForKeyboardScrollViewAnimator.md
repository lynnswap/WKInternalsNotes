# ``WKInternalsNotes/WKKeyboardScrollViewAnimatorDelegate/isScrollableForKeyboardScrollViewAnimator(_:)``

キーボードスクロール可能かを判定する。

## Objective-C Declaration
```objective-c
- (BOOL)isScrollableForKeyboardScrollViewAnimator:(WKKeyboardScrollViewAnimator *)animator;
```

## Discussion
`WKContentView` では、編集可能状態や select フィールドのフォーカス中、`scrollEnabled` が `NO` の場合に `NO` を返す。`allowsKeyboardScrolling` が存在する環境ではその値も確認する。

## References
- [`WKKeyboardScrollingAnimator.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.h#L62)
- [`WKContentViewInteraction.mm#L7835`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7835)
- [`WKContentViewInteraction.mm#L7837`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7837)
- [`WKContentViewInteraction.mm#L7843`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7843)
- [`WKContentViewInteraction.mm#L7847`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7847)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
