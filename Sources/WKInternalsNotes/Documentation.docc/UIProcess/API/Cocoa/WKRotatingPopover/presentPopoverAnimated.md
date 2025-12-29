# ``WKInternalsNotes/WKRotatingPopover/presentPopoverAnimated(_:)``

ポップオーバーを表示する。

## Objective-C Declaration
```objective-c
- (void)presentPopoverAnimated:(BOOL)animated;
```

## Discussion
`presentationPoint` が未設定なら `focusedElementInformation.interactionRect` を使い、設定済みならページスケールを掛けた座標を使う。表示領域と交差しない場合は何もしない。Mac Catalyst ではフォーカス引き渡しを開始し、`presentPopoverFromRect:inView:` で表示する。

## References
- [`WKFormPopover.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPopover.h#L36)
- [`WKFormPopover.mm#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPopover.mm#L117)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
