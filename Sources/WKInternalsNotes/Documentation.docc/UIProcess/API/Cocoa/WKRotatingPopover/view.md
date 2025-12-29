# ``WKInternalsNotes/WKRotatingPopover/view``

ポップオーバーを表示する基準ビュー。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKContentView *view;
```

## Default Value
`nil`（`initWithView:` で設定される）。

## Discussion
`initWithView:` で受け取った `WKContentView` を保持し、表示位置計算に使用する。

## References
- [`WKFormPopover.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPopover.h#L35)
- [`WKFormPopover.mm#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPopover.mm#L81)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
