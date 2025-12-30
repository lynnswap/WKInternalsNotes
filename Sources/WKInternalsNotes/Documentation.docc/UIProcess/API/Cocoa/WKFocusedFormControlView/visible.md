# ``WKInternalsNotes/WKFocusedFormControlView/visible``

明示的な実装がなく、自動合成のフラグとして扱われる。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isVisible) BOOL visible;
```

## Default Value
自動合成のため初期値は `NO`。

## Discussion
`show:` / `hide:` は `hidden` と `alpha` を操作するだけで `visible` は更新していない。

## References
- [`WKFocusedFormControlView.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L68)
- [`WKFocusedFormControlView.mm#L140`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L140)
- [`WKFocusedFormControlView.mm#L157`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L157)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
