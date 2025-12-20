# ``WKInternalsNotes/WKKeyboardScrollViewAnimator/beginWithEvent(_:scrollView:)``

キーボードイベントによるスクロール開始を試みる。

## Objective-C Declaration
```objective-c
- (BOOL)beginWithEvent:(::WebEvent *)event scrollView:(WKBaseScrollView *)scrollView;
```

## Discussion
`scrollView` が未設定なら保持し、別のスクロールビューが渡された場合は `NO` を返す。`_animator` の `beginWithEvent` を呼び、`Began` の場合のみ `YES` を返す。キーがスクロールをトリガしない場合は `_scrollView` を `nil` に戻して `NO` を返す。

## References
- [`WKKeyboardScrollingAnimator.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.h#L47)
- [`WKKeyboardScrollingAnimator.mm#L612`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L612)
- [`WKKeyboardScrollingAnimator.mm#L614`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L614)
- [`WKKeyboardScrollingAnimator.mm#L620`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L620)
- [`WKKeyboardScrollingAnimator.mm#L621`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L621)
- [`WKKeyboardScrollingAnimator.mm#L627`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L627)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
