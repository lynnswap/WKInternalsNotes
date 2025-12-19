# ``WKInternalsNotes/WKContentView/_removeTemporaryDirectoriesWhenDeallocated(_:)``

破棄時に削除する一時ディレクトリを登録する。

## Objective-C Declaration
```objective-c
- (void)_removeTemporaryDirectoriesWhenDeallocated:(Vector<RetainPtr<NSURL>>&&)urls;
```

## Discussion
渡された URL を `_temporaryURLsToDeleteWhenDeallocated` に追加する。

## References
- [`WKContentView.h#L123`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L123)
- [`WKContentView.mm#L538`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L538)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
