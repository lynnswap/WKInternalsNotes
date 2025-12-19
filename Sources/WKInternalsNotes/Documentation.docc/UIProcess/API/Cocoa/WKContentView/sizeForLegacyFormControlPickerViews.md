# ``WKInternalsNotes/WKContentView/sizeForLegacyFormControlPickerViews``

レガシーなフォームピッカー用のサイズを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGSize sizeForLegacyFormControlPickerViews;
```

## Default Value
ウィンドウ幅を使い、高さは既定の inputView 高さに委ねる。

## Discussion
`self.window.bounds.size` をベースに高さを `0` にして返す（入力ビューの既定高さにフォールバックさせるため）。

## References
- [`WKContentViewInteraction.h#L742`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L742)
- [`WKContentViewInteraction.mm#L13546`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L13546)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
