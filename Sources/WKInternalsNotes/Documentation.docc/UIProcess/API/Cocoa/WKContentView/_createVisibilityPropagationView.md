# ``WKInternalsNotes/WKContentView/_createVisibilityPropagationView()``

可視性伝播ビューを生成して登録する。

## Objective-C Declaration
```objective-c
- (UIView *)_createVisibilityPropagationView;
```

## Discussion
`WKVisibilityPropagationView` を生成して保持集合に追加し、各プロセス向けの伝播設定を行ったうえで返す。

## References
- [`WKContentView.h#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L117)
- [`WKContentView.mm#L972`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L972)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
