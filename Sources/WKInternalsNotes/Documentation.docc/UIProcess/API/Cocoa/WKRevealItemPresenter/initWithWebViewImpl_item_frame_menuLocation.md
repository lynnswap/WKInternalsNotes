# ``WKInternalsNotes/WKRevealItemPresenter/initWithWebViewImpl(_:item:frame:menuLocation:)``

Reveal 表示用のプレゼンタを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithWebViewImpl:(const WebKit::WebViewImpl&)webViewImpl item:(RVItem *)item frame:(CGRect)frameInView menuLocation:(CGPoint)menuLocationInView;
```

## Discussion
`WebViewImpl` を弱参照で保持し、`RVPresenter` と `RVPresentingContext` を生成する。`RVPresentingContext` は `menuLocationInView` と `view` を使って生成し、`highlightDelegate` に自身を設定する。`item` と表示位置を保持して初期化を完了する。

## References
- [`WKRevealItemPresenter.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKRevealItemPresenter.h#L41)
- [`WKRevealItemPresenter.mm#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKRevealItemPresenter.mm#L52)
- [`WKRevealItemPresenter.mm#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKRevealItemPresenter.mm#L57)
- [`WKRevealItemPresenter.mm#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKRevealItemPresenter.mm#L60)
- [`WKRevealItemPresenter.mm#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKRevealItemPresenter.mm#L61)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
