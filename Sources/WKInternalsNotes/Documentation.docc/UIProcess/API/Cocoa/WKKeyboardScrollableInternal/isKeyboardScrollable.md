# ``WKInternalsNotes/WKKeyboardScrollableInternal/isKeyboardScrollable()``

キーボードスクロールを許可するかどうかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)isKeyboardScrollable;
```

## Discussion
delegate が `isScrollableForKeyboardScrollViewAnimator:` に応答できる場合はその結果を返す。未実装の場合は `YES`。

## References
- [`WKKeyboardScrollingAnimator.mm#L651`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L651)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
