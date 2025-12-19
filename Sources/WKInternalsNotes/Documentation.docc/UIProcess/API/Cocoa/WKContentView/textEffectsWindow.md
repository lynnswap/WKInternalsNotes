# ``WKInternalsNotes/WKContentView/textEffectsWindow()``

現在の windowScene に紐づく text effects window を返す。

## Objective-C Declaration
```objective-c
- (UIView *)textEffectsWindow;
```

## Discussion
`UITextEffectsWindow sharedTextEffectsWindowForWindowScene:` を使って `self.window.windowScene` の共有ウィンドウを返す。

## References
- [`WKContentViewInteraction.h#L955`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L955)
- [`WKContentViewInteraction.mm#L11595`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11595)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
