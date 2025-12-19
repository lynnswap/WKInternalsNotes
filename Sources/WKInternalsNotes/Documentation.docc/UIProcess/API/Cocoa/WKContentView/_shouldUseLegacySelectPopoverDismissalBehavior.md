# ``WKInternalsNotes/WKContentView/_shouldUseLegacySelectPopoverDismissalBehavior``

select のポップオーバーを旧挙動で閉じるべきかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _shouldUseLegacySelectPopoverDismissalBehavior;
```

## Default Value
小画面でないこと、`InputType::Select` であること、Data Activation 条件が揃うことが前提。

## Discussion
Data Activation 環境で `select` がフォーカスされた場合のみ `YES` を返す。

## References
- [`WKContentViewInteraction.h#L943`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L943)
- [`WKContentViewInteraction.mm#L10228`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10228)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
