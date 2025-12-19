# ``WKInternalsNotes/WKContentView/_createTargetedPreviewFromTextIndicator(_:previewContainer:)``

テキストインジケータからターゲットプレビューを生成する。

## Objective-C Declaration
```objective-c
- (UITargetedPreview *)_createTargetedPreviewFromTextIndicator:(RefPtr<WebCore::TextIndicator>&&)textIndicator previewContainer:(UIView *)previewContainer;
```

## Discussion
`textIndicator` が無ければ `nil` を返す。`contentImage` から画像を生成し、文字矩形と背景色推定値を使って `UITargetedPreview` を作成する。背景色が透明の場合はシステム背景色を使う。

## References
- [`WKContentViewInteraction.h#L956`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L956)
- [`WKContentViewInteraction.mm#L11671`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11671)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
